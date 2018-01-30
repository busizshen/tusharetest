import tensorflow as tf

# 定义一个32位浮点数的变量，初始值位0.0
v1 = tf.Variable(dtype=tf.float32, initial_value=0.)

# 衰减率decay，初始值位0.99
decay = 0.99

# 定义num_updates，同样，初始值位0
num_updates = tf.Variable(0, trainable=False)

# 定义滑动平均模型的类，将衰减率decay和num_updates传入。
ema = tf.train.ExponentialMovingAverage(decay=decay, num_updates=num_updates)

# 定义更新变量列表
update_var_list = [v1]

# 使用滑动平均模型
ema_apply = ema.apply(update_var_list)

# Tensorflow会话
with tf.Session() as sess:
    # 初始化全局变量
    sess.run(tf.global_variables_initializer())

    # 输出初始值
    print(sess.run([v1, ema.average(v1)]))
    # [0.0, 0.0]（此时 num_updates = 0 ⇒ decay = .1, ），
    # shadow_variable = variable = 0.

    # 将v1赋值为5
    sess.run(tf.assign(v1, 5))

    # 调用函数，使用滑动平均模型
    sess.run(ema_apply)

    # 再次输出
    print(sess.run([v1, ema.average(v1)]))
    # 此时，num_updates = 0 ⇒ decay =0.1,  v1 = 5;
    # shadow_variable = 0.1 * 0 + 0.9 * 5 = 4.5 ⇒ variable

    # 将num_updates赋值为10000
    sess.run(tf.assign(num_updates, 10000))

    # 将v1赋值为10
    sess.run(tf.assign(v1, 10))

    # 调用函数，使用滑动平均模型
    sess.run(ema_apply)

    # 输出
    print(sess.run([v1, ema.average(v1)]))
    # decay = 0.99,shadow_variable = 0.99 * 4.5 + .01*10 ⇒ 4.555

    # 再次使用滑动平均模型
    sess.run(ema_apply)

    # 输出
    print(sess.run([v1, ema.average(v1)]))
    # decay = 0.99，shadow_variable = .99*4.555 + .01*10 = 4.609
    for i in range(1000):
        sess.run(ema_apply)
        print(sess.run([v1, ema.average(v1)]))