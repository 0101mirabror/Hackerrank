def cannons_ready(gunners):
    return 'Fire!' if len(gunners)==len(list(filter(lambda x: x=='aye', gunners.values()))) else 'Shiver me timbers!'
# best
# def cannons_ready(gunners):
#   return 'Shiver me timbers!' if 'nay' in gunners.values() else 'Fire!'
ls = []
