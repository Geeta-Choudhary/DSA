def designerPdfViewer(h, word):
    # Write your code here
    max_height = 0
    for i in word:
        index=ord(i) -ord('a')
        height = h[index]
        if height > max_height :
            max_height = height
    return max_height * len(word)
    