import csv


def stringtoint(stringdate):
    first = stringdate.split("T")[0]
    second = first.split("-")
    year = int(second[0])
    month = int(second[1])
    day = int(second[2])
    return year, month, day


def monthday_array():
    """
    helper function for days_uploaded
    """
    monthday = [31, 0]
    for i in range(7, 0, -1):
        if i % 2 == 1:
            monthday.insert(0, monthday[0] + 31)
        elif i == 2:
            monthday.insert(0, monthday[0] + 28)
        else:
            monthday.insert(0, monthday[0] + 30)
    for i in range(9, 12):
        if i == 11:
            monthday.append(monthday[-1] - 31)
        else:
            monthday.append(monthday[-1] - 30)
    monthday.insert(0, 0)
    return monthday


monthday = monthday_array()
#print (monthday)


def days_uploaded(year, month, day):
    # assuming each year has 365 days
    days = (2018 - year) * 365

    days += monthday[month]

    days += 15 - day

    return days


x,y,z = stringtoint("2017-01-13T17:13:01.000Z")
#print(x,y,z)
#print(days_uploaded(x, y, z))
#print(days_uploaded(2017, 1, 13)), "expected: 610"

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
            x,y,z = stringtoint(url_dict[url][4])
            publishing_time = days_uploaded(x, y, z)

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
    csv_file = open('combined4.csv', 'w')
    writer = csv.writer(csv_file)
    writer.writerow(["video_id", "publish_time","views", "likes", "dislikes", "comment_count","new_views", "new likes", "new dislikes", "new comment_count", "views_change", "likes_change", "dislikes_change", "comment_count_change"])
    for key, value in vid_dict.items():
        value.insert(0, key)
        writer.writerow(value)

    csv_file.close()

new_cvs("USvideos.csv", "new_vid_data.csv")