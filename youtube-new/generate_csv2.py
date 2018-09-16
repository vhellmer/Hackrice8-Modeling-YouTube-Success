import csv

def new_cvs(original_stats, new_stats):

    new_data = csv.reader(open(new_stats))
    old_data = csv.reader(open(original_stats))

    print(new_data)

    # create list of all url in new_data
    # create mapping of url in new_data to their views
    url_list = []
    new_url_dict = {}
    count1 = 0
    for list in new_data:
        if count1 != 0:
            try:
                new_url_dict[list[0]] = [float(list[1].replace(',','')), float(list[2].replace(',', '')), float(list[3].replace(',','')), float(list[4].replace(',',''))]
                url_list += [list[0]]
            except:
                print(list[0], " failed")
        count1 += 1

    # create mapping of url in old data to all its other stats
    url_dict = {}
    count2 = 0
    for list in old_data:
        if count2 != 0:
            url_dict[list[0]] = list[1:]
        count2 += 1

    # fill in the stats for all the url in
    vid_dict = {}
    for url in url_list:
        if url in url_dict:

            # publish time, views, likes, dislikes, comment_count
            publishing_time = url_dict[url][4]
            views = float(url_dict[url][6])
            likes = float(url_dict[url][7])
            dislikes = float(url_dict[url][8])
            comment_count = float(url_dict[url][9])
            new_views = new_url_dict[url][0]
            new_likes = new_url_dict[url][1]
            new_dislikes = new_url_dict[url][2]
            new_comment_count = new_url_dict[url][3]
            views_change = new_views - views
            likes_change = new_likes - likes
            dislikes_change = new_dislikes - dislikes
            comment_count_change = new_comment_count - comment_count

            if new_views != 0:
                vid_dict[url] = [publishing_time, views, likes, dislikes, comment_count, new_views, new_likes, new_dislikes, new_comment_count, views_change, likes_change, dislikes_change, comment_count_change]

    # create the csv file
    csv_file = open('combined2.csv', 'w')
    writer = csv.writer(csv_file)
    writer.writerow(["video_id", "publish_time","views", "likes", "dislikes", "comment_count","new_views", "new likes", "new dislikes", "new comment_count", "views_change", "likes_change", "dislikes_change", "comment_count_change"])
    for key, value in vid_dict.items():
        value.insert(0, key)
        writer.writerow(value)

    csv_file.close()

new_cvs("USvideos.csv", "new_vid_data.csv")