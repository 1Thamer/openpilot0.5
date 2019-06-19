import time
from selfdrive.df import df_wrapper
df_model = df_wrapper.df_wrapper()
df_model.init_model()
start = time.time()
#for i in range(50):
model_output = df_model.run_model(0.8653078153514447,
 0.46805728618371273,
 0.28780443294609244,
 0.01075646532123655)
#print(time.time() - start)
print(model_output)