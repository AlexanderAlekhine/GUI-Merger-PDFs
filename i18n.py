# Configuración de idiomas
languages = {
    'en': {
        'button_add': 'Add',
        'button_delete': 'Delete',
        'button_create': 'Create PDF',
    },
    'es': {
        'button_add': 'Añadir',
        'button_delete': 'Eliminar',
        'button_create': 'Crear PDF',
    },
    'fr': {
        'button_add': 'Ajouter',
        'button_delete': 'Supprimer',
        'button_create': 'Créer PDF',
    },
    'de': {
        'button_add': 'Hinzufügen',
        'button_delete': 'Löschen',
        'button_create': 'PDF erstellen',
    },
    'it': {
        'button_add': 'Aggiungi',
        'button_delete': 'Elimina',
        'button_create': 'Crea PDF',
    },
    'pt': {
        'button_add': 'Adicionar',
        'button_delete': 'Excluir',
        'button_create': 'Criar PDF',
    },
    'ru': {
        'button_add': 'Добавить',
        'button_delete': 'Удалить',
        'button_create': 'Создать PDF',
    },
    'zh': {
        'button_add': '添加',
        'button_delete': '删除',
        'button_create': '创建PDF',
    },
    'ja': {
        'button_add': '追加',
        'button_delete': '削除',
        'button_create': 'PDFを作成',
    },
    'ko': {
        'button_add': '추가',
        'button_delete': '삭제',
        'button_create': 'PDF 만들기',
    }
}

class Translator:
    def __init__(self, language):
        self.language = language

    def gettext(self, message):
        # Busca la traducción en el diccionario
        return languages[self.language].get(message)