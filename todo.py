#!/Users/aki/VScodeWorkspace/Python/Flask/env03/bin/python3
# -*- coding: utf-8 -*-


class ToDoItem:
    item_id = 0

    def __init__(self, title):
        self.title = title
        self.done = False
        self.item_id = ToDoItem.item_id


class ToDoList:
    def __init__(self):
        self.todolist = []
#追加

    def add(self, title):
        item = ToDoItem(title)
        ToDoItem.item_id += 1
        self.todolist.append(item)


#削除
    def delete(self, item_id):
        self.todolist = [x for x in self.todolist if x.item_id != item_id]


#更新
    def update(self, item_id):
        item = [x for x in self.todolist if x.item_id == item_id]
        item[0].done = not item[0].done

#todo項目を含むリスト
    def get_all(self):
        return self.todolist


# 完了済み削除

    def delete_doneitem(self):
        self.todolist = [x for x in self.todolist if not x.done]
