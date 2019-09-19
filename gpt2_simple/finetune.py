import gpt_2_simple as gpt2

model_name = "355M"
gpt2.download_gpt2(model_name=model_name)   # model is saved into current directory under /models/117M/

sess = gpt2.start_tf_sess()
gpt2.finetune(sess,
              '../../Data/movies.txt',
              model_name=model_name,
	      run_name='movies',
              steps=10000) # steps is max number of training steps

gpt2.generate(sess)
