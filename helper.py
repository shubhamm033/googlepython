# filename='alice.txt'

# file=open(filename,'r')

# for steps in file:
#     print(steps.split())



def word_count_dict(filename):
  """Returns a word/count dict for this filename."""
  # Utility used by count() and Topcount().
  word_count = {}  # Map each word to its count
  input_file = open(filename, 'r')
  for line in input_file:
    #print(line)
    words = line.split()
    for word in words:
      word = word.lower()
      
      # Special case if we're seeing this word for the first time.
      if word in word_count:
        word_count[word] =word_count[word] + 1
      else:
        word_count[word] = 1
    #print(word_count)
    
   # print(word_count)
  input_file.close()  # Not strictly required, but good form.
  return word_count



   
# def print_count(filename):
#   word_count=word_count_dict(filename)
#   words=sorted(word_count.keys())
#   for word in words:
#     print word, word_count[word]

def get_count(word_count_tuple):
  return word_count_tuple[1]

def print_top(filename):

  word_count=word_count_dict(filename)
  items=sorted(word_count.items(),key=get_count,reverse=1)
  print(items)

  for item in items[:20]:
    print item[0],item[1]
  
print_top('alice.txt')