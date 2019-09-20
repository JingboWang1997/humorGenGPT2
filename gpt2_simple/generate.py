import gpt_2_simple as gpt2

sess = gpt2.start_tf_sess()
print('Start Generating')
prefixes = ['Nurse Chang discusses the progress of her research on the planet, and the thought of a female Human',
            'However, when she overrules him, the Doctor realizes that the Doctor has been wrong, stating that',
            "A team of undercover security personnel from the FBI infiltrate a warehouse in a warehouse in Los Angeles' Central"]
gpt2.load_gpt2(sess, run_name='run1')
for prefix in prefixes:
    print('\nprefix:\n',prefix)
    for i in range(3):
        gpt2.generate(sess, length=100, prefix=prefix);
        print('\n')
		
