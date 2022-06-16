# Usd-Python-Reference
一个纯手打的usd python api参考文档
因为usd api只有C++的，所以打算做个一个usd python的中文api文档。
文档内容包括类继承关系，函数参数，解释，example代码等等
更新时间不定（看自己学到哪就写到哪）
中英文混用，请忽视my poor English

最近发现，当我想要某个类的一些属性的时候，很难找得到，（比如layer上的文件路径），stage.GetLayerStack()获取之后只是得到一个Sdf.Find("z:/path")的一个包含了我想要的数据的类，但这个Sdf layer类怎么转到我想要的string path，我看了好久的c++ api都没有找得到。最后在偶然的情况下，我看到help(Sdf.Layer)之后，发现这个类上有个property叫realPath，然后我试着打印一下，就拿到我想要的string path了。这种情况让我深思，之前拿到类上的数据一直都是找求值的函数，没想过api直接把值写在里面了（主要是C++文档没有提过这会事），一下子思路打开，做个中文的usd python参考指南越发重要了。
