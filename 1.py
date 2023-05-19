import requests 
 

r = requests.get('http://127.0.0.1:8000/hotels/12', params ={"date_from":"today"})

print(r)