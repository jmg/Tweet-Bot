# Tweet-Bot 

### Setup your own bot!

----------------------------------------------------------

Go to https://dev.twitter.com/apps and create an **application on twitter**.
Just follow the instructions and you will get **four authentication keys**.

When you get those keys just open the **settings.py** file and put them into
the **auth dictionary**

```python
auth = {
    "CONSUMER_KEY" : "YOUR_CONSUMER_KEY",
    "CONSUMER_SECRET" : "YOUR_CONSUMER_SECRET",
    
    "ACCESS_TOKEN" : "YOUR_ACCESS_TOKEN",
    "ACCESS_TOKEN_SECRET" : "YOUR_ACCESS_TOKEN_SECRET",
}
```
----------------------------------------------------------

Now you can **feed your bot**. Open the **tweets.txt** file and write **one tweet
per line**. Ensure the line don't be over more than **140 chars**.

-----------------------------------------------------------

**Done!** Just run (to teewt once):

```bash
~$ python bot.py 
```

or to tweet **forever** each **10** minutes:

```bash
~$ python bot.py -t 10
```

