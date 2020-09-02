import pygame
import pygame_gui
import MySQLdb
import game_db


pygame.init() #initialize all imported pygame modules
pygame.display.set_caption('Cybersquare')
window_surface = pygame.display.set_mode((800, 600))
background = pygame.Surface((800, 600))
background.fill(pygame.Color('#ffffff'))

logged_user = ""

manager = pygame_gui.UIManager((800, 600), "theme.json")


# Start screen for selecting login or registration
panel_select= pygame_gui.elements.ui_panel.UIPanel(pygame.Rect((150, 200), (550, 150)), 
                                                manager= manager, starting_layer_height=3)

btn_show_login=pygame_gui.elements.UIButton(relative_rect=pygame.Rect((100, 50), (100, 25)), text='Login',
                                                manager=manager, container=panel_select)

btn_show_register=pygame_gui.elements.UIButton(relative_rect=pygame.Rect((300, 50), (100, 25)), text='Register',
                                                manager=manager, container=panel_select)


# Registration form -  full name, Username/ email id, password, Gender
panel_reg = pygame_gui.elements.ui_panel.UIPanel(pygame.Rect((150, 100), (550, 400)), 
                                                manager= manager, starting_layer_height=2)

lbl_name = pygame_gui.elements.ui_label.UILabel(relative_rect= pygame.Rect((50, 50), (200, 25)), 
                                                manager= manager, text="Full name", container=panel_reg)
txt_name = pygame_gui.elements.ui_text_entry_line.UITextEntryLine(relative_rect= pygame.Rect((300,50), (200, 50)), 
                                                                manager= manager, container=panel_reg)

lbl_uname = pygame_gui.elements.ui_label.UILabel(relative_rect= pygame.Rect((50, 100), (200, 25)), container=panel_reg,
                                                manager= manager, text="Email/ Username" )
txt_username = pygame_gui.elements.ui_text_entry_line.UITextEntryLine(relative_rect= pygame.Rect((300, 100), (200, 50)), 
                                                manager= manager, container=panel_reg)

lbl_passwrod = pygame_gui.elements.ui_label.UILabel(relative_rect= pygame.Rect((50, 150), (200, 25)), container=panel_reg,
                                                manager= manager, text="Password")
txt_password = pygame_gui.elements.ui_text_entry_line.UITextEntryLine(relative_rect= pygame.Rect((300, 150), (200, 50)), 
                                                manager= manager, container=panel_reg)

lbl_gender = pygame_gui.elements.ui_label.UILabel(relative_rect= pygame.Rect((50, 200), (200, 25)), container=panel_reg,
                                                manager= manager, text="Gender")
dd_lst_gender = pygame_gui.elements.ui_drop_down_menu.UIDropDownMenu(relative_rect= pygame.Rect((300, 200), (200, 25)), 
                                                manager= manager, options_list=["male", "female"],
                                                starting_option="male", container=panel_reg)
btn_signup = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((250, 250), (100, 25)), text='Sign up',
                                                manager=manager, container=panel_reg)

# Panel to display registration success
panel_reg_msg = pygame_gui.elements.ui_panel.UIPanel(pygame.Rect((40, 280), (450, 70)), 
                                                manager= manager, starting_layer_height=3, container=panel_reg)
lbl_reg_message = pygame_gui.elements.ui_label.UILabel(relative_rect= pygame.Rect((5, 5), (300, 25)), container=panel_reg_msg,
                                                manager= manager, text="You have registered successfully")
btn_play_game = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((300, 5), (100, 25)), text='Play game',
                                                manager=manager, container=panel_reg_msg)
panel_reg_msg.hide()
panel_reg.hide()



# Login panel
panel_login = pygame_gui.elements.ui_panel.UIPanel(pygame.Rect((150, 100), (550, 250)), 
                                                manager= manager, starting_layer_height=1)

lbl_luname = pygame_gui.elements.ui_label.UILabel(relative_rect= pygame.Rect((50, 50), (200, 25)), container=panel_login,
                                                manager= manager, text="Email/ Username" )
txt_lusername = pygame_gui.elements.ui_text_entry_line.UITextEntryLine(relative_rect= pygame.Rect((300, 50), (200, 50)), 
                                                manager= manager, container=panel_login)

lbl_lpasswrod = pygame_gui.elements.ui_label.UILabel(relative_rect= pygame.Rect((50, 100), (200, 25)), container=panel_login,
                                                manager= manager, text="Password")
txt_lpassword = pygame_gui.elements.ui_text_entry_line.UITextEntryLine(relative_rect= pygame.Rect((300, 100), (200, 50)), 
                                                manager= manager, container=panel_login)
btn_login = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((250, 150), (100, 25)), text='Login',
                                                manager=manager, container=panel_login)
lbl_login_msg = pygame_gui.elements.ui_label.UILabel(relative_rect= pygame.Rect((100, 180), (250, 25)), container=panel_login,
                                                manager= manager, text="Incorrect username or password")                                                
panel_login.hide()


is_running = True
clock = pygame.time.Clock()

# Game loop for event handling
while is_running:
    time_delta = clock.tick(60)/1000.0
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False

        if event.type == pygame.USEREVENT:
            if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                if event.ui_element == btn_signup:
                    print(txt_name.get_text())
                    print(dd_lst_gender.selected_option)

                if event.ui_element == btn_show_login:
                    panel_select.hide()
                    panel_login.show()
                    lbl_login_msg.hide()

                if event.ui_element == btn_show_register:
                    panel_select.hide()
                    panel_reg.show()
                    panel_reg_msg.hide()

                if event.ui_element == btn_signup:
                    name = txt_name.get_text()
                    username = txt_username.get_text()
                    user_password = txt_password.get_text()
                    gender = dd_lst_gender.selected_option
                    print(name, username, user_password, gender)
                    result = game_db.register(username, user_password, name, gender)
                    
                    if result:
                        logged_user = username
                        panel_reg_msg.show()
                    else:
                        pass

                if event.ui_element == btn_login:
                    username = txt_lusername.get_text()
                    user_password = txt_lpassword.get_text()
                    result=game_db.login(username, user_password)
                    
                    if result:
                        print("Login success")
                    else:
                        lbl_login_msg.show()
                        print("Login fail")

                if event.ui_element == btn_play_game:
                        print("You can play th game")
                        print(txt_username.get_text())
                    

        manager.process_events(event)
    manager.update(time_delta)
    window_surface.blit(background, (0, 0))
    manager.draw_ui(window_surface)
    pygame.display.update()








# CREATE TABLE tbl_user(
# user_id INT AUTO_INCREMENT,
# username VARCHAR(100) unique,
# password VARCHAR(200),
# full_name VARCHAR(200),
# gender VARCHAR(200),
# PRIMARY KEY(user_id)
# );
