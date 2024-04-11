import csv                                                                      
                                                                                
def get_characters():                                                           
    url = "https://rickandmortyapi.com/api/character/"                          
    params = {                                                                  
        "species": "Human",                                                     
        "status": "Alive",                                                      
        "origin": "Earth"                                                       
    }                                                                           
                                                                                
    try:                                                                        
        response = requests.get(url, params=params)                             
        data = response.json()                                                  
                                                                                
        if "results" in data:                                                   
            characters = data["results"]                                        
                                                                                
            # Write results to a CSV file                                       
            with open("rick_and_morty_characters.csv", "w", newline="") as csvfile:
                fieldnames = ["Name", "Location", "Image Link"]                 
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)         
                writer.writeheader()                                            
                                                                                
                for character in characters:                                    
                    writer.writerow({                                           
                        "Name": character["name"],                              
                        "Location": character["location"]["name"],              
                        "Image Link": character["image"]                        
                    })                                                          
                                                                                
            print("Results written to rick_and_morty_characters.csv")           
        else:                                                                   
            print("No characters found.")                                       
    except requests.RequestException as e:                                      
        print(f"Error fetching data: {e}")                                      
                                                                                
if __name__ == "__main__":                                                      
    get_characters()
