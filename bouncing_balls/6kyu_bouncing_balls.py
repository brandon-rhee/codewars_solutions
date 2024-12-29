def bouncing_ball(h, bounce, window):
    if not (h > 0 and 0 < bounce < 1 and window < h):
        return -1
    count = 1
    current_height = h*bounce

    while current_height > window:
        count += 2
        current_height *= bounce
    return count

print(bouncing_ball(30, 0.66, 1.5))

