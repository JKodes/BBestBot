import searching.search_buy 



#run = searching.search_buy.Searching()
#run.main_page()

with searching.search_buy.Searching() as done:
    done.main_page()
    done.type_item_of_choice('portable air Conditioner')
    done.click_button()
    done.add_to_cart()
    done.go_to_cart()
    done.checkout()
    done.returning_customer_email('')  #email for people who already have an account, but not signed in
    done.returning_customer_password('') #password for people who already have an account, but not signed in
