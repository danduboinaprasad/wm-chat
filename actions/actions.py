# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from ctypes import Union
from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.forms import FormValidationAction
from rasa_sdk.events import SlotSet, SessionStarted, ActionExecuted, EventType,AllSlotsReset
from rasa_sdk.types import DomainDict


class FindCode(Action):

     def name(self) -> Text:
         return "find_code_action"

    
    
     def run(self, dispatcher: CollectingDispatcher,
             tracker: Tracker,
             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

         dispatcher.utter_message(text="you can check here [website](https://rasa.com/docs/rasa/nlu-training-data)")

         return [AllSlotsReset()]

class FindPoc(Action):

     def name(self) -> Text:
         return "find_poc_action"

    
    
     def run(self, dispatcher: CollectingDispatcher,
             tracker: Tracker,
             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

         dispatcher.utter_message(text="you can touch with Alex")

         return [AllSlotsReset()]