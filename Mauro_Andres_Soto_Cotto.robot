*** Settings ***
Library  SeleniumLibrary



*** Variables ***




*** Test Cases ***
LoginTest
    # Browse to React shopping cart demo.

    # Opening Browser

    Open Browser    https://react-shopping-cart-67954.firebaseapp.com/  chrome
    Sleep    3s
    # 2. Use the size filter to select size M and add to cart 1 shirt
    Click Element    xpath=//*[@id="root"]/div/main/div/div[1]/div[3]/label/span
    Sleep    1s
    Click Element    //button[contains(text(),'Add to cart')]
    Sleep    2s
    #Close cart
    Click Element    //body/div[@id='root']/div[1]/div[1]/button[1]

    # Use the size filter to unselect M size and select L size.
    Click Element    //body/div[@id='root']/div[1]/main[1]/div[1]/div[1]/div[3]/label[1]/span[1]
    Sleep    1s
    Click Element    //body/div[@id='root']/div[1]/main[1]/div[1]/div[1]/div[5]/label[1]/span[1]
    Sleep    1s

    # Compulsively add 6 shirts to your cart.
    FOR    ${counter}    IN RANGE    0    6    
        Click Element    //body/div[@id='root']/div[1]/main[1]/main[1]/div[1]/div[1]/button[1]
         
    END
    Sleep    1s
    # Come back to your senses and delete 4 shirts from your cart.
    FOR    ${counter}    IN RANGE    0    4    
        Click Element    //body/div[@id='root']/div[1]/div[1]/div[1]/div[2]/div[2]/div[2]/div[1]/button[1]
    END
    Sleep    1s
    # Click checkout button.
    Click Element    //button[contains(text(),'Checkout')]
    


*** Keywords ***
