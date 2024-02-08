def insertion_sort(l)
  # enumerate over list
  l.each_with_index do |current_value, i=1|
    if current_value > l[i - 1]
      # no changes need to be made
    else
      while i > 0 && current_value < l[i - 1]
        l[i] = l[i - 1]
        i = i - 1
      end
    end
    l[i] = current_value
  end
  return l
end

def main()
  test_list = [9, 5, 3, 7, 2, 8, 4, 1, 6, 0]

  puts "unsorted:"
  print "#{test_list}\n"
  puts "sorted:"
  print insertion_sort(test_list)
end


main()
