<script setup lang="ts">
import { ref } from 'vue';
import { databaseMutateProtected } from '../tools/databaseTools';
const CARD = ref({
  cardName: "",
  cardSet: "",
  cardRarity: "",
  cardType: "",
  cardSubType: "",
  cardClass: "",
  cardTwoSided: false,
  cardFront: false,
  cardArt: "",
  cardWeaponType: "",
  cardHands: false,
  cardPitchValue: 0,
  cardRed: false,
  cardYellow: false,
  cardBlue: false,
  cardAttack: 0,
  cardDefense: 0,
  cardAB: false,
  cardABValue: 0,
  cardBattleworn: false,
  cardBoost: false,
  cardDominate: false,
  cardGoAgain: false,
  cardHeave: false,
  cardHeaveValue: 0,
  cardIntimidate: 0,
  cardLegendary: false,
  cardOpt: false,
  cardOptValue: 0,
  cardPhantasm: false,
  cardPierce: false,
  cardPierceValue: 0,
  cardQuell: false,
  cardQuellValue: 0,
  cardReload: false,
  cardSpectra: false,
  cardSpellvoid: false,
  cardSpellvoidValue: 0,
  cardTemper: false,
  cardWard: false,
  cardWardValue: 0,
  cardAttackAct: false,
  cardAttackActText: "",
  cardAttackReact: false,
  cardAttackReactText: "",
  cardInstantAct: false,
  cardInstantActText: "",
  cardDefenseAct: false,
  cardDefenseActText: "",
  cardChannel: false,
  cardChannelText: "",
  cardCombo: false,
  cardComboText: "",
  cardContract: false,
  cardContractText: false,
  cardCrush: false,
  cardCrushText: "",
  cardEssence: false,
  cardEssenceText: "",
  cardFusion: false,
  cardFusionText: "",
  cardMaterial: false,
  cardMaterialText: "",
  cardReprise: false,
  cardRepriseText: "",
  cardRupture: false,
  cardRuptureText: "",
  cardSpecialization: false,
  cardSpecializationText: "",
})

const blurEvents = () => {
  if (CARD.value.cardRed == true) {
    CARD.value.cardYellow = false
    CARD.value.cardBlue = false
    return;
  }
  if (CARD.value.cardYellow == true) {
    CARD.value.cardRed = false
    CARD.value.cardBlue = false
    return;
  }
  if (CARD.value.cardBlue == true) {
    CARD.value.cardRed = false
    CARD.value.cardYellow = false
    return;
  }
}

const stringCard = async () => {
  let body: string = JSON.stringify(CARD.value)
  let body_: FormData = new FormData();
  body_.append("sdfuh", "suidh");
  body_.append("sdf", "sdfh");
  console.log(body_);
  console.log(body)
  let r = await databaseMutateProtected("cards", body, "POST")
  console.log(r)
}

</script>

<template>
  <w-flex column justify-center class="wrapper">
    <w-form>
      <w-button @click="stringCard()">Stringify</w-button>
      <div v-for="value, item in CARD">
        <div v-if="typeof value == 'string'">
          <h5> {{ item }}</h5>
          <w-input v-model="CARD[item]"></w-input>
        </div>
        <div v-if="typeof value == 'boolean'">
          <h5> {{ item }}</h5>
          <w-checkbox v-model="CARD[item]"></w-checkbox>
        </div>
        <div v-if="typeof value == 'number'">
          <h5> {{ item }}</h5>
          <w-input type="number" v-model="CARD[item]"></w-input>
        </div>
      </div>
    </w-form>
  </w-flex>
</template>