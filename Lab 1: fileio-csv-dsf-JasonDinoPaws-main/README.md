# Lab 1: File I/O and CSVs
## Caesar Cipher
A Caesar cipher, or a shift cipher, is one of the simplest encryption techniques. This method is named after Julius Caesar who would use it to send private messages. To encrypt information with a Caesar cipher, each letter in your message or plaintext is replaced by a letter a fixed numbers of positions away in the alphabet to generate your ciphertext. 

For example, if I wanted to encrypt the message `ECHO` using a left shift of 3, I would rewrite each character by shifting the entire alphabet left by 3 characters. Using the chart and key below, we can see that `E -> B`, `C -> Z`, `H -> E`, and `O -> L`. So `ECHO` becomes `BZEL`.
![Pasted image 20231227102315](https://github.com/gormes-EPIC/FileIO-CSV-DSF/assets/134316348/36015604-5669-475c-a8c6-3d4674da98d4)

Plaintext:  ABCDEFGHIJKLMNOPQRSTUVWXYZ
Ciphertext: XYZABCDEFGHIJKLMNOPQRSTUVW

We can use the same cipher to encrypt the plaintext `THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG` as the ciphertext `QEB NRFZH YOLTK CLU GRJMP LSBO QEB IXWV ALD`. Then decrypt it using our key in the other direction and shifting right by 3.

As long as whoever is reading the message knows you have shifted the alphabet left by 3, it is straightforward to decrypt `BZEL` as `ECHO`. But what if you intercepted this message and didn't know the original shift? By exploiting patterns in the English language, we can actually decrypt Caesar ciphers without knowing the original shift. [Source](https://www.101computing.net/caesar-cipher/)

### Letter Frequency
One way to break a Caesar cipher is to look at the frequency of the letters. In a typical English text, some letters are much more frequent that others. 

Using [Project Gutenburg](https://www.gutenberg.org/) download at least 3 books into your Jupyter Notebook. *Hint: Once you navigate to a book, copy the URL of the Plain Text UTF-8 download and user the `wget` command in your Jupyter terminal.* Then, read in all of your books, count each of the letters, and create a frequency table. After you are done, print out the information. 
#### Example
```
A: 1023
B: 356
C: 40
...
```

### Challenge: Break this Caesar Cipher
Decode the following ciphertext. Start by creating a frequency table of the letters in the ciphertext and matching the most popular letters with the letters from above. *Tip: In addition to using your letter frequency table from above to help you, look at the 1 and 2 letter words carefully. There are limited options those characters could be! Also, look try to identify frequently used words like `THE` or `AND` in your ciphertext.*

Ciphertext:
```
PA PZ H WLYPVK VM JPCPS DHY. YLILS ZWHJLZOPWZ, ZAYPRPUN MYVT H OPKKLU IHZL, OHCL DVU AOLPY MPYZA CPJAVYF HNHPUZA AOL LCPS NHSHJAPJ LTWPYL. KBYPUN AOL IHAASL, YLILS ZWPLZ THUHNLK AV ZALHS ZLJYLA WSHUZ AV AOL LTWLYVY'Z BSAPTHAL DLHWVU, AOL KLHAO ZAHY, HU HYTVYLK ZWHJL ZAHAPVU DPAO LUVBNO WVDLY AV KLZAYVF HU LUAPYL WSHULA. WBYZBLK IF AOL LTWLYVY'Z ZPUPZALY HNLUAZ, WYPUJLZZ SLPH YHJLZ OVTL HIVHYK OLY ZAHYZOPW, JBZAVKPHU VM AOL ZAVSLU WSHUZ AOHA JHU ZHCL OLY WLVWSL HUK YLZAVYL MYLLKVT AV AOL NHSHEF ....
```

## Log Files
One important way for businesses to keep themseleves secure is to monitor their server logs.

Read in `server_log.txt` containing server access logs with entries like "IP Address-Timestamp-Page Accessed".
- Count the total number of unique IP addresses that accessed the server.
- Identify the top three most accessed pages.
- Generate a report file "server_summary.txt" containing this information.

## Receiptify
The application [Receiptify](https://receiptify.herokuapp.com/) connects to your Spotify account and generates a receipt themed report of your listening history for the past week. You are going to build a worse version of this for your lab. 

Read in the CSV file `spotify_data.csv`. The data will be listed in the CSV in the format `song,artist,date,time`. Once you have calculated the top 10 songs, list them in a receipt format. You will probably want to format the output using [tabulate](https://pypi.org/project/tabulate/) but you can also print it out by hand.

```
|-----------------------------|
|       NOT RECEIPTIFY        |
|          Last Week          |
|_____________________________|
|QTY|ITEM                 |AMT|
|-----------------------------|
|01  Dancing Queen          48|

```
