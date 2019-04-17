aa = "aa"
p aa
alph = ("a".."z").to_a            # create array with alphabet
caesar = puts.chomp                 # input string to cypher
caesar.split('').each do |i|         # itterate on string to cypher
  puts alph[alph.index(i).to_i + 2]  # replace character fron string with 2 position higher (a -> c)
end

####### JUST DISCOVERED - HOW TO OPERATE ON BLOCK RESULTS ##########
####### BELOW - EXAMPLE. NOT FULLY WORKING CODE #############
[2,4,6,8,10].each{|i| p i}        ## this returns [2,4,6,8,10] array
[2,4,6,8,10].each{|i| p i}.join   ## this returns string made of .joined array !
##############              \__add operator after block to change what's returned !

# yield maxic example
def yy arr,a
  arr.each{|i| p "#{yield i} - #{a}"; a = a.next}
end

# Xmass tree
30.times {|i| puts " "*(30-i) + "X"*i*2}

Time.now   # returns curent time
Date.today   # return current date
required 'date'  # must load this first to make date.today working

# not sure whats that?

%w { 1 2 3 4 }.each do |num|
s3_file "/usr/local/tomcat7-7/part[num].tif"
remote_path "part[num].tif"
bucket "perftest-data"
aws_access_key_id "XXXXXXX"
aws_secret_access_key "ZZZZZZZZ"
owner "root"
group "root"
mode "0644"
action :create
end
