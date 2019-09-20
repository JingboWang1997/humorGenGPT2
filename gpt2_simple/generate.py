import gpt_2_simple as gpt2

sess = gpt2.start_tf_sess()
print('Start Generating')
gpt2.load_gpt2(sess, run_name='scifi')
for i in range(3):
#    gpt2.generate(sess, length=20);
#    print('\n')
    gpt2.generate(sess, length=100, prefix="At least he didn't yell at her -- I told her he didn't have a heart of stone");
		
