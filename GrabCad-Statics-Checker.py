from bs4 import BeautifulSoup
import requests
import tkinter as tk





wid = tk.Tk()


l3 = tk.Label(wid,text='Result will be showed here', font=('times', 12 , 'bold'))
l3.grid(row=1, column=0, columnspan=2, padx=7, pady=10)


def get_url():      
    some = url_entry.get()
    new_some = some.rstrip().strip("\n")
    new_some = new_some.replace(" ",".").lower()
    base_url = "https://grabcad.com/"
    end_url = "-1"
    url = base_url+new_some+end_url
    result = get_grabcadscore(url)

    if result:
        result_text = "\n".join(result)
        l3.config(text=result_text)
        



def get_grabcadscore(url):

    

    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}
    try:
        page = requests.get(url, headers=headers)
        if page.status_code == 200:
            soup = BeautifulSoup(page.text, 'html.parser')
            #print(soup.prettify())
            ta1 = soup.find('table')
            ta2 = ta1.findAll('tr')
            ta3 = [title.text.strip()  for title in ta2]
            ta4 = [ites.replace("\n",": ") for ites in ta3]
            ta4 = [ites.replace("::",": ") for ites in ta4]
            return(ta4)
        else:
            print(f"Failed to retrieve the page, status code: {page.status_code}")

    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")



wid.title('View Grabcad Profile Statistics')
wid.geometry('450x300')


l1 = tk.Label(wid,text='User Name: ').grid(row=0,column=0, padx=7,pady=20)
url_entry = tk.Entry(wid,width=55)
url_entry.grid(row=0,column=1,padx=1,pady=30)


getprofiele = tk.Button(wid, text="Get Profile", command=get_url)
getprofiele.grid(row=2, column=0, columnspan=2, pady=20)

wid.mainloop()