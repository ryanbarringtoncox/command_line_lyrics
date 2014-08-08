#!/usr/bin/ruby
require 'ruby-web-search'

search_string = ARGV.join(" ")
#puts search_string

response = RubyWebSearch::Google.search(:query => search_string, :size => 10)

for r in response.results
  puts r[:url]
end

