# image = image file_path
# caption = image caption

def post_image_and_caption(image, caption):
    import tweepy

    # Authorization Tokens
    access_token = '1262556492944859136-8IxvNboeBljh2fai0OcZNsam7bCXTb'
    access_token_secret = 'OGWw8x0joaYIkT2plG7QF8rnFQbgTwRHl0oDIeBDB261C'
    consumer_key = '1vxukZQuIkjeTgxj7f77GngvK'
    consumer_secret = 'KPfV1JRvc1FcoVmGkOkZcv5y5CfBT2OGO41m1LoYej6I3bUuUw'

    # Authenticate to Twitter
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    # Create API object
    api = tweepy.API(auth)

    # Upload image
    media = api.media_upload(image)

    # Post tweet with image
    post_result = api.update_status(status=caption, media_ids=[media.media_id])


if __name__ == "__main__":

    #Using function independently
    image = input("input an image path")
    caption = input("Write a Caption")
    post_image_and_caption(image, caption)
