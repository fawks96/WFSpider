# WFSpider
A spider for Wanfang database

&ensp;

- **爬取对象**

  [万方数据库](http://www.wanfangdata.com.cn/index.html)
  
  ![Demo0](https://raw.githubusercontent.com/fawks96/WFSpider/master/Demo%20pictures/Demo0.png)
  
 &ensp;
  
- **爬取逻辑**

  从一级主站出发，遍历二级期刊，以期刊为基点，获取该期刊中的所有文章。对应的爬虫模块为WFbase、WFindex和WFcore。
  
  以文章为元单位，它的主要属性包括：文章标题、文章摘要、文章作者、文章所属刊物名、文章出版日期、文章关键字等。
  
  ![Demo1](https://raw.githubusercontent.com/fawks96/WFSpider/master/Demo%20pictures/Demo1.png)
    
  对空数据进行删除，对不符合格式要求的异常文章或字段进行删除处理。最后将整理好的数据以csv格式文件导出。
  
  ![Demo2](https://raw.githubusercontent.com/fawks96/WFSpider/master/Demo%20pictures/Demo2.png)

&ensp;

- **结果检索系统**

  根据爬取结果建立一个小型检索系统WF Search，它支持根据文章标题、作者、摘要、全文等进行搜索，还支持热门关键词文章搜索。
  
  ![Demo3](https://raw.githubusercontent.com/fawks96/WFSpider/master/Demo%20pictures/Demo3.png)
  
  此项目为：
