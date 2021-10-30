# https://www.codewars.com/kata/563fbac924106b8bf7000046
# Breadcrumb Generator

# First Implementation 15/10/2021
def getShortCrumb(newCrumb):   
    shortCrumb=""
    currentWord=""
    for letter in newCrumb:
        if letter == "-":
            if currentWord not in ["the","of","in","from","by","with","and", "or", "for", "to", "at", "a"]:
                shortCrumb+=currentWord[0].upper()
            currentWord=""
        else:
            currentWord+=letter
    if currentWord not in ["the","of","in","from","by","with","and", "or", "for", "to", "at", "a"]:
        shortCrumb+=currentWord[0].upper()
    return shortCrumb

def generate_bc(url, separator):
    a = '<a href="/"></a>' + separator
    span = '<span class="active"></span>'
    breadcrumb=a[:12] + "HOME" + a[12:]
    if url[0:4] == "http":
        url=url[8:]
    
    for letter in url:
        url=url[1:]
        if letter == "/":
            break
    
    indexPos=url.find("index")
    if indexPos != -1:
        if indexPos == 0:
            url=""
        else:
            url=url[:indexPos-1]
            
    if url == "":
        return '<span class="active">HOME</span>'
    
    completeCrumb=""
    newCrumb=""
    for letter in url:
        if letter == "/":
            completeCrumb+=newCrumb+"/"
            
            if len(newCrumb) > 30:
                newCrumb=getShortCrumb(newCrumb)
            newCrumb=newCrumb.replace("-", " ")
            breadcrumb+=a[:10] + completeCrumb + '">' + newCrumb.upper() + a[12:]    
            newCrumb=""
        else:
            newCrumb+=letter
            url=url[1:]
            
    newCrumb, url = "", newCrumb
    
    for letter in url:
        if letter in [".", "?", "#"] :
            if len(newCrumb) > 30:
                newCrumb=getShortCrumb(newCrumb)
            newCrumb=newCrumb.replace("-", " ")
            breadcrumb+=span[:21] + newCrumb.upper() + span[21:]    
            break
        if len(url) == 1:
            newCrumb+=letter
            if len(newCrumb) > 30:
                newCrumb=getShortCrumb(newCrumb)
            newCrumb = newCrumb.replace("-", " ")
            breadcrumb+=span[:21] + newCrumb.upper() + span[21:]    
            break
            
        newCrumb+=letter
        url=url[1:]
        
    return breadcrumb 