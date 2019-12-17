# Textmining and Topic Modelling

A social news website by the name Hacker News (https://news.ycombinator.com/news) was used for this activity.

## Tasks Performed
1. Most recent 500 articles were extracted from the new site using web scraping and put into a data frame.
    * **title** - Title of the post
    * **date_created** - date and time the post was created
    * **user_name** - name of the account that made the post
    * **link_title** - url of the post
    * **domain** - domain like github.com, medium.com etc
    * **up_points** - number of upvotes the post received
    * **comment_number** - number of comments the post received
    
Extraction was performed using **BeautifulSoup**. Exception handling was also done in case there were any missing values. Once the data was extracted, the dataframe was converted to a csv file to avoid making continuous requests.

2. For each url of the post the body of the paragraph was extracted.
> A function was written to go to each of the links and extract the paragraph tags from the webpage. Along with requests **header** was also passed to avoid **403 error**.

3. Topic modelling was performed.
    * **SVD** was performed on the **document term matrix.**
    * On the SVD transformed matrix **Kmeans clustering** was performed to obtain the number of topics.
    * Each cluster was names based on the understanding.
    * Five Articles in each of the cluster were displayed.
