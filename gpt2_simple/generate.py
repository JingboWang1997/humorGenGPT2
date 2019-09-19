import gpt_2_simple as gpt2

print('generating');
sess = gpt2.start_tf_sess()
gpt2.load_gpt2(sess)

gpt2.generate(sess, prefix="Could you please tell me how you're defining 'scandalous mark'? From your brief, I thought you were giving it a different definition than")




