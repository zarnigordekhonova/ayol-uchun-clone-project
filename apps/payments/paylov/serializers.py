from rest_framework import serializers

from apps.payments.paylov.constants import PaylovMethods


class PaylovSerializer(serializers.Serializer):
    '''
    Bu serializer Paylov tranzaksiya ma'lumotlari bilan ishlaydi.
    '''

    id: serializers.IntegerField = serializers.IntegerField()
    method: serializers.ChoiceField = serializers.ChoiceField(
        choices=PaylovMethods.choices
    )
    params: serializers.JSONField = serializers.JSONField()