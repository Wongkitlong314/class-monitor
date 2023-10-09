import httpx
from app.config.config import ACCESSTOKEN, BASEURL, RECIPIENT, BUSSINESS
import asyncio
import json

class BasicResponse:
    def __init__(self, text=None, data=None, recipient=None, **kwargs):
        self.text = text if text else ""
        self.data = {
                "platform" : "WA",
                "from" : BUSSINESS,
                "to" : RECIPIENT,
                "type" : "text",
                "text" : self.text
            }
        if recipient:
            self.data["to"] = recipient
        if data:
            self.data.update(data)
        self.headers = {
            'Authorization': 'Bearer ' + ACCESSTOKEN,
            'Content-Type': 'application/json'
        }
        self.endpoint = "/message"

    async def send(self):
        data = json.dumps(self.data)
        async with httpx.AsyncClient() as client:
            response = await client.post(BASEURL + self.endpoint, data=data, headers=self.headers)
            return response.text
    
    def change_recipient(self, recipient):
        self.data["to"] = recipient

class TextResponse(BasicResponse):
    def __init__(self, text, **kwargs):
        super().__init__(text, **kwargs)

class ButtonResponse(BasicResponse):
    def __init__(self, text, buttons, header=None, image_url=None, file_url=None, footer=None, **kwargs):
        super().__init__(text, **kwargs)
        self.data["type"] = "button"
        self.data["buttons"] = buttons
        if footer:
            self.data["footer"] = footer
        # can't use two types at the same time
        assert not (header and file_url) and not (header and image_url) and not (file_url and image_url)
        if header:
            self.data["headerType"] = "text"
            self.data["header"] = header
        if file_url:
            self.data["headerType"] = "document"
            self.data["mediaURL"] = file_url
        if image_url:
            self.data["headerType"] = "image"
            self.data["mediaURL"] = image_url

class ListResponse(BasicResponse):
    def __init__(self, text, listTitle, listData, descriptionData=None, **kwargs):
        super().__init__(text, **kwargs)
        self.data["type"] = "list"
        self.data["listTitle"] = listTitle
        self.data["listData"] = listData
        if descriptionData:
            data = list()
            for i in range(len(listData)):
                item = dict()
                item["title"] = listData[i]
                item["description"] = descriptionData[i]
                data.append(item)
            self.data["listData"] = data

class BasicMediaResponse(BasicResponse):
    def __init__(self, mediaURL, mediaType, text=None, **kwargs):
        super().__init__(text, **kwargs)
        self.data.pop("type")
        self.data["mediaType"] = mediaType
        self.endpoint = "/message/media"
        if mediaURL.startswith("http"):
            response = httpx.get(mediaURL)
            self.files = {'file': (mediaURL.split('/')[-1], response.content, 'application/octet-stream')}
        else:
            self.files=[('file', (mediaURL.split('/')[-1], open(mediaURL,'rb'), 'application/octet-stream'))]
        self.headers['Content-Type'] = 'multipart/form-data; boundary=----'

    async def send(self):
        async with httpx.AsyncClient() as client:
            response = await client.post(BASEURL + self.endpoint, data=self.data, headers=self.headers, files=self.files)
            return response.text

class ImageResponse(BasicMediaResponse):
    def __init__(self, image_url,**kwargs):
        super().__init__(image_url, "image", **kwargs)

class VideoResponse(BasicMediaResponse):
    def __init__(self, video_url, **kwargs):
        super().__init__(video_url, "video", **kwargs)

class AudioResponse(BasicMediaResponse):
    def __init__(self, audio_url, **kwargs):
        super().__init__(audio_url, "audio", **kwargs)

class DocumentResponse(BasicMediaResponse):
    def __init__(self, document_url, **kwargs):
        super().__init__(document_url, "document", **kwargs)

if __name__ == "__main__":
    response = TextResponse("Hello World!")
    response = ButtonResponse("Hello World!", ["Button1", "Button2"])
    response = ListResponse("Hello World!", "List Title", ["text1", "text2"])
    response = ImageResponse("https://www.google.com/images/branding/googlelogo/2x/googlelogo_color_272x92dp.png")
    response = VideoResponse("https://www.learningcontainer.com/wp-content/uploads/2020/05/sample-mp4-file.mp4")
    response = AudioResponse("https://www.learningcontainer.com/wp-content/uploads/2020/02/Kalimba.mp3")
    response = DocumentResponse("https://browse.arxiv.org/pdf/2306.00026.pdf")
    text = asyncio.run(response.send())
    print(text)
