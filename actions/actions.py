# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet
from pymystem3 import Mystem

class ActionItemAdded(Action):

    def name(self) -> Text:
        return "action_item_added"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        i_list = tracker.get_slot("items_list")
        new_item = tracker.get_slot("item")
        m = Mystem()
        new_item = m.lemmatize(new_item)[0]
        if not i_list:
            i_list = [new_item]
        else:
            i_list.append(new_item)
        dispatcher.utter_message(response="utter_item_added")

        return [SlotSet("items_list", i_list)]


class ActionShowItems(Action):

    def name(self) -> Text:
        return "action_show_items"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        i_list = tracker.get_slot("items_list")
        resp = "Ваша корзина:" + " ".join(i_list)
        dispatcher.utter_message(text=resp)

        return []
