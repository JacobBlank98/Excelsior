# image = image file_path
# caption = image caption

def post_image_and_caption(image, caption):
    import tweepy

    # Authorization Tokens
    access_token = '1858668422-cQsfg6zTjRXnMErfbVkPTBQfRpz3wA0HTWbjUUB'
    access_token_secret = 'pWrVpJvGQB37p24e62e4oDNMopYYTqv6WgWkft5K6z1dR'
    consumer_key = 'pfoaSCz63ceQQWHoEJY3MEjAA'
    consumer_secret = 'siPmdQLwDrJN8RTkuf4tals7HFIAwnkjpmKLAXLnLAJGqIgEfg'

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
    post_image_and_caption()
