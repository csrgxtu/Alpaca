from mrjob.job import MRJob
from mrjob.protocol import PickleProtocol, TextValueProtocol


class ImgSimMRJOB(MRJob):
    INPUT_PROTOCOL = PickleProtocol

    def mapper(self, _, line):
        yield 'archer', 1

    def reducer(self, key, values):
        yield key, sum(values)


if __name__ == '__main__':
    ImgSimMRJOB.run()
