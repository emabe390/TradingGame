
incrementing_identifier = 0

def next_id():
    global incrementing_identifier
    myid = incrementing_identifier
    incrementing_identifier += 1
    return myid