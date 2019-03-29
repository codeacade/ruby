# Calculate time needed to grow bacteria population.
# Bacteria population (ba) doubles every one hour (bh)
# Set what population you need (max), and computer
# will calculate how long you have to wait (bh).
def bacteria(max)
  ba = 1
  bh = 0
  while(ba<max) do
	ba = ba*2
	bh +=1
	print bh
	print " - "
	puts ba
  end
  return bh
 end

puts "[ PRESS ENTER ]"
a = gets
