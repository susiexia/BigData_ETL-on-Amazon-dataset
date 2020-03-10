"""The classic MapReduce job: count the frequency of words.
 We use python and MRJob library to practice smaller scale dataset, 
 in oder to understand the underlying of Hadoop MapReduce

There are 6 steps to word count in MapReduce
 Input -> Splitting -> Mapping -> shuffling -> reducing -> final result

--------EXAMPLE------------------------------------

from mrjob.job import MRJob
import re

WORD_RE = re.compile(r"[\w']+")

class MRWordFreqCount(MRJob):

    def mapper(self, _, line):
        for word in WORD_RE.findall(line):
            yield (word.lower(), 1)

    def combiner(self, word, counts):
        yield (word, sum(counts))

    def reducer(self, word, counts):
        yield (word, sum(counts))

if __name__ == '__main__':
     MRWordFreqCount.run()

-------execute------------------
# locally
python mrjob/examples/mr_word_freq_count.py README.rst > counts
"""

# import library
from mrjob.job import MRJob

class Bacon_count(MRJob):    # Our Objedct inherits MRJob object properties
    # splitting and mapping step
    def mapper(self, _, line):
        for word in line.split():
            if word.lower() == "bacon":
  # use yield continue producing a list of elements, return only return once
                yield "bacon", 1

    # the shuffling step performed by MRJob, no code

    # reducing step
    def reducer(self, key, values):
        yield key, sum(values)

# run this object directly on python cli
if __name__ == "__main__":
    Bacon_count.run()

# run code in terminal
# python practice_mrjob.py input.txt 
# or python practice_mrjob.py input.txt > values