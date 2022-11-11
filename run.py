import searching.search_buy 



#run = searching.search_buy.Searching()
#run.main_page()

with searching.search_buy.Searching(teardown=True) as done:
    done.main_page()