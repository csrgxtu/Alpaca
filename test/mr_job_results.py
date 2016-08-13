from mrjob.job import MRJob

class MRWordCounter(MRJob):
    def mapper(self, key, line):
        results = []
        for word in line.split():
            results.append((word, 1))
        return results

    def reducer(self, word, occurrences):
        yield word, sum(occurrences)

# if __name__ == '__main__':
#     res = MRWordCounter.run()
