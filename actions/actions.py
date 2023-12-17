# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet

class ActionItemAdded(Action):

    def name(self) -> Text:
        return "action_item_added"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        i_list = tracker.get_slot("items_list")
        new_item = tracker.get_slot("item")

        print(i_list)
        print(type(i_list))
        print(new_item)
        print()
        if not i_list:
            i_list = [new_item]
            print(11111)
        else:
            i_list.append(new_item)
        print(i_list)
        dispatcher.utter_message(response="utter_item_added")

        return [SlotSet("items_list", i_list)]
