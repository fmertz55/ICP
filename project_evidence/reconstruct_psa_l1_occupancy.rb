#!/usr/bin/env ruby
# frozen_string_literal: true

# Reconstruct a common-resolution occupancy table from an adaptive PSA voxel
# snapshot. Parent cells retain pre-subdivision sentences while later arrivals
# enter descendants, so mixed-level labels must be aggregated to a common
# ancestor before a marginal rank analysis.

require "csv"
require "json"

abort "usage: #{$PROGRAM_NAME} SNAPSHOT_JSON [TARGET_LEVEL]" if ARGV.empty?

snapshot_path = ARGV.fetch(0)
target_level = Integer(ARGV.fetch(1, "1"))
snapshot = JSON.parse(File.read(snapshot_path))
voxels = snapshot.fetch("voxels")

rows = Hash.new do |hash, key|
  hash[key] = {
    "stored_at_target" => 0,
    "stored_below_target" => 0,
    "descendant_cells" => 0
  }
end

input_total = 0

voxels.each do |label, record|
  match = label.match(/(?:^|:)L(\d+)_v_(-?\d+)_(-?\d+)_(-?\d+)$/)
  abort "unrecognized voxel label: #{label}" unless match

  level, x, y, z = match.captures.map(&:to_i)
  abort "cannot aggregate level #{level} upward to finer L#{target_level}" if level < target_level

  count = Integer(record.fetch("sentences"))
  input_total += count
  factor = 2**(level - target_level)
  ancestor = "L#{target_level}_v_#{x.div(factor)}_#{y.div(factor)}_#{z.div(factor)}"

  if level == target_level
    rows[ancestor]["stored_at_target"] += count
  else
    rows[ancestor]["stored_below_target"] += count
    rows[ancestor]["descendant_cells"] += 1
  end
end

output_total = rows.values.inject(0) do |sum, record|
  sum + record["stored_at_target"] + record["stored_below_target"]
end
abort "mass mismatch: input=#{input_total}, output=#{output_total}" unless input_total == output_total

CSV($stdout) do |csv|
  csv << %w[
    target_voxel
    stored_at_target
    stored_in_descendants
    reconstructed_count
    descendant_cells
    has_descendants
  ]

  rows.sort_by do |label, record|
    [-(record["stored_at_target"] + record["stored_below_target"]), label]
  end.each do |label, record|
    reconstructed = record["stored_at_target"] + record["stored_below_target"]
    csv << [
      label,
      record["stored_at_target"],
      record["stored_below_target"],
      reconstructed,
      record["descendant_cells"],
      record["descendant_cells"].positive?
    ]
  end
end

warn "reconstructed #{rows.size} L#{target_level} cells; total mass #{output_total}"
