from mr_word_count import MRWordFrequencyCount

res = {}
mr_job = MRWordFrequencyCount()
with mr_job.make_runner() as runner:
    runner.run()
    for line in runner.stream_output():
        key, value = mr_job.parse_output_line(line)
        # print key, value
        res[key] = value

print res
