import csv
import datetime
import os

from dotenv import find_dotenv, load_dotenv
import instagrapi


load_dotenv(find_dotenv())

class Instagram_Api:
    def __init__(self, output_path, verification_code):
        # Environment Variables
        self.username = os.environ.get('INSTAGRAM_USERNAME')
        self.password = os.environ.get('INSTAGRAM_PASSWORD')
        
        # Paths
        self.output_path = output_path
        
        # API Variables
        self.client = None
        self.verification_code = verification_code
        
    def login(self):
        self.client = instagrapi.Client()
        self.client.login(self.username, self.password, verification_code=self.verification_code)
        
    def get_userid_from_username(self, username: str) -> int:
        if not self.client:
            self.login()
        return self.client.user_id_from_username(username=username)
    
    def get_username_from_userid(self, userid: int) -> str:
        if not self.client:
            self.login()
        return self.client.username_from_user_id(user_id=userid)
    
    def search_user(self, userid: int):
        if not self.client:
            self.login()
        return self.client.user_info(str(userid))
    
    def download_images(self, userid):
        """
        Right now: Download up to 10 images
        Future: Download images that were uploaded today
        """
        media_list = self.client.user_medias(user_id=userid, amount=10)
        cnt = 0
        for media in media_list:
            if media.media_type == 1:
                self.client.photo_download(media_pk=media.pk, folder=self.output_path)
                cnt += 1
            if media.media_type == 8:
                for resource in media.resources:
                    if resource.media_type == 1:
                        self.client.photo_download(media_pk=resource.pk, folder=self.output_path)
                        cnt += 1
        
        return cnt 

def get_account_list(csv_path):
    lst = []
    with open(csv_path, newline='') as csvfile:
        rows = csv.DictReader(csvfile)
        for row in rows:
            lst.append(row['Account'])
    
    return lst
    
if __name__ == "__main__":
    csv_file = '../Accounts/instagram_accounts.csv'
    account_list = get_account_list(csv_file)
    
    x = Instagram_Api('../Images/To_Analyze', '430723')
    x.login()
    
    for name in account_list:
        print('Start: {}'.format(name))
        id = x.get_userid_from_username(name)
        download_cnt = x.download_images(userid=id)
        print('Downloaded: {}'.format(download_cnt))
        break