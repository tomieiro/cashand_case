## Seleção de idioma / Language selection ######################################
##
## Permite ao jogador escolher o idioma do jogo logo que ele é aberto pela
## primeira vez. A escolha fica gravada nas preferências do Ren'Py (persistente
## entre execuções), então esta tela só aparece uma vez. O idioma também pode
## ser trocado depois, na tela de Preferências.
##
## Lets the player choose the game language the first time the game is opened.
## The choice is stored in Ren'Py's preferences (persisted across launches), so
## this screen only shows once. The language can also be changed later from the
## Preferences screen.

## Flag persistente que indica se o jogador já escolheu um idioma.
default persistent.lang_chosen = False

init python:

    def is_english():
        """Retorna True quando o idioma ativo e o ingles.

        Usada no lugar de checar config.language diretamente para que os textos
        embutidos no codigo (puzzles, notificacoes, etc.) acompanhem o idioma
        escolhido em tempo de execucao."""
        return _preferences.language == "english"


## Tela de seleção de idioma exibida na abertura do jogo.
screen language_select():

    tag menu
    modal True

    add gui.main_menu_background
    add Solid("#000000a0")

    vbox:
        align (0.5, 0.5)
        spacing 30

        text "Selecione o idioma\nSelect the language":
            xalign 0.5
            text_align 0.5
            color gui.accent_color
            size 40

        null height 20

        textbutton "Português":
            xalign 0.5
            text_size 32
            action Return("none")

        textbutton "English":
            xalign 0.5
            text_size 32
            action Return("english")


## Label de abertura: mostra a seleção de idioma apenas na primeira execução.
label splashscreen:

    if not persistent.lang_chosen:

        call screen language_select

        $ persistent.lang_chosen = True

        if _return == "english":
            $ _preferences.language = "english"
        else:
            $ _preferences.language = None

        $ renpy.change_language(_preferences.language)

    return
