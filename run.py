import searching.search_buy 



#run = searching.search_buy.Searching()
#run.main_page()

with searching.search_buy.Searching() as done:
    done.main_page()
    done.type_item_of_choice('Air Conditioner')
    done.click_button()
    done.add_to_cart()
    done.go_to_cart()
    done.checkout()