# Page value ranges from 0 to 33
# Selector = <.detname a>
def generator_oppo(topic,pages):
    import requests , bs4 ,  os, winshell 

    def createFolder(directory):
        try:
            if not os.path.exists(directory):
                os.makedirs(directory)
        except OSError:
            print ('Error: Creating directory. ' +  directory)  

    desktop = winshell.desktop()
    createFolder(os.path.join(desktop, topic.capitalize()))
    
    path = os.path.join(desktop, topic+"\\Results_for_"+topic.capitalize()+".html")
    path2 = os.path.join(desktop, topic+"\\style.css")

    html_file = open("index.html")

    contents_html_file = html_file.read()


    new_file = open(path, 'w')
    new_file.write(contents_html_file)

    css_file = open("style.css")
    final_css_file = open(path2, 'w')
    final_css_file.write(css_file.read())

    for index , pages in enumerate(range(0,pages)):
        res_html = requests.get('https://thepiratebay.org/user/'+topic+'/'+ str(index) +'/3//')
        res_html.raise_for_status()

#https://thepiratebay.org/user/tuts756/5/3


        res_parsed = bs4.BeautifulSoup(res_html.text,features = "lxml")
        listed_name = res_parsed.select('div .detName a')

        if not (listed_name == []):
            for counts , objects in enumerate(listed_name):
                obj = listed_name[counts]
                obj_name = obj.getText() 
                obj_link = obj.get('href')
                with_dash_test = (((obj_name[:8].upper()).replace(" ",'') == 'UDEMY-' )or (obj_name[:6].upper()== 'UDEMY-'))
                without_dash_test = obj_name[:6].upper() == 'UDEMY '
                
                if ((with_dash_test and without_dash_test) or with_dash_test):
                    obj_name = obj_name.replace('Udemy - ',"")
                    obj_name = obj_name.replace('UDEMY - ',"")
                    obj_name = obj_name.replace('UDEMY-',"")

                elif without_dash_test:
                    obj_name = obj_name.replace('Udemy ',"")
                
                new_file.write(r'<div class="rep_tiles"><div id="text">'+str(counts+1)+'. '+ obj_name + r'</div><div id = "btns"><a href ="https://thepiratebay.org'+obj_link+'" ><button id="download">Download</button></a></div></div>')
        else:
            print("Done")
            break

    new_file.write('</div></body></html>')
    new_file.close()
            # <a href ="https://thepiratebay.org'+obj_link+'">'+obj_name+'</a>