stage是用来打开usd文件，一般用法是stage = Usd.Stage.Open(usd_file)
有时候usd文件内容因为层层包含会非常大，有个小技巧可以不加载
stage = Usd.Stage.Open(usd_file, load=Usd.Stage.LoadNone)
