<template>
	<teleport to="body">
		<Modal class="userModal" :show="showModal" :title="title" @close="$emit('close')">
			<form class="form" :class="isSignUp ? 'form_wide' : ''">
				<template v-if="isSignUp">
					<div class="form__row">
						<label class="form__field form__field_alert">
							<AppInput v-model="userData.name" type="text" placeholder="Введите Имя *" required />
							<span class="form__error alert alert_small alert_danger">Имя обязательно для заполнения</span>
						</label>
						<label class="form__field">
							<AppInput v-model="userData.surname" type="text" placeholder="Введите Фамилию" />
						</label>
					</div>
					<div class="form__row">
						<label class="form__field form__field_alert">
							<AppInput v-model="userData.email" type="email" placeholder="Введите эл. почту *" autocomplete="username" required />
							<span class="form__error alert alert_small alert_danger">Эл. почта обязательно для заполнения</span>
						</label>
						<label class="form__field form__field_alert">
							<AppInput v-model="userData.phone" type="phone" placeholder="Введите телефон *" mask="+7 (###)-###-##-##" required />
							<span class="form__error alert alert_small alert_danger">Телефон обязательно для заполнения</span>
						</label>
					</div>
					<div class="form__row">
						<label class="form__field">
							<AppInput v-model="userData.city" type="email" placeholder="Введите город" />
						</label>
						<label class="form__field">
							<AppInput v-model="userData.street" type="email" placeholder="Введите улицу" />
						</label>
					</div>
					<div class="form__row">
						<label class="form__field">
							<AppInput v-model="userData.house" type="email" placeholder="Введите номер дома" />
						</label>
						<label class="form__field">
							<AppInput v-model="userData.apartment" type="email" placeholder="Введите номер квартиры" />
						</label>
					</div>
					<div class="form__row">
						<label class="form__field form__field_alert">
							<AppInput v-model="userData.password" type="password" placeholder="Введите пароль *" autocomplete="new-password" required />
							<span class="form__error alert alert_small alert_danger">Пароль обязательно для заполнения</span>
						</label>
						<label class="form__field form__field_alert">
							<AppInput v-model="userData.passwordRetry" type="password" placeholder="Повторите пароль *" autocomplete="new-password" required />
							<span class="form__error alert alert_small alert_danger">Пароль обязательно для заполнения</span>
						</label>
					</div>
				</template>
				<template v-else>
					<label class="form__field form__field_alert">
						<AppInput v-model="userData.email" type="email" placeholder="Введите эл. почту *" autocomplete="username" required />
						<span class="form__error alert alert_small alert_danger">Эл. почта обязательно для заполнения</span>
					</label>
					<label class="form__field form__field_alert">
						<AppInput v-model="userData.password" type="password" placeholder="Введите пароль *" autocomplete="current-password" required />
						<span class="form__error alert alert_small alert_danger">Пароль обязательно для заполнения</span>
					</label>
				</template>
			</form>
			<template #footer>
				<template v-if="isSignUp">
					<AppButton class="userModal__button" color="white" :icon="true" @click="isSignUp = false">
						<template #icon>
							<ArrowLeftIcon fill="none" />
						</template>
						Назад
					</AppButton>
					<AppButton class="userModal__button" color="secondary" @click="valid">Зарегистрироваться</AppButton>
				</template>
				<template v-else>
					<AppButton class="userModal__button" color="secondary" @click="$emit('close')">Войти</AppButton>
					<AppButton class="userModal__button" color="white" @click="isSignUp = true">Нет еще аккаунта? Зарегистрируйтесь</AppButton>
				</template>
			</template>
		</Modal>
	</teleport>
</template>

<script lang="ts">
import { defineComponent, ref, computed, Ref } from 'vue';
import Modal from '@/components/modal.vue';
import AppInput from '@/components/form/input.vue';
import AppButton from '@/components/button/index.vue';
import ArrowLeftIcon from '@/components/icons/arrowLeftIcon.vue';
import { UserAuthI } from '@/api/user/types';

export default defineComponent({
	name: 'userModal',
	emits: ['close'],
	props: {
		showModal: {
			type: Boolean,
			default: false,
		},
	},
	setup() {
		const isAuth = ref(false);
		const isSignUp = ref(true);
		const title = computed(() => isSignUp.value ? 'Регистрация' : 'Вход в личный кабинет');

		// todo Сделать валидацию
		const userData: Ref<UserAuthI> = ref({
			name: '',
			surname: '',
			email: '',
			phone: '',
			password: '',
			passwordRetry: '',
			city: '',
			street: '',
			house: '',
			apartment: '',
		});

		function valid() {
			console.log(userData.value);
		}

		return {
			isAuth,
			isSignUp,
			title,
			userData,
			valid,
		};
	},
	components: {
		Modal,
		AppInput,
		AppButton,
		ArrowLeftIcon,
	},
});
</script>

<style lang="scss" scoped>
@import '@/assets/css/modules/var';
@import '@/assets/css/components/form';
@import '@/assets/css/components/alert';

.userModal {
	&__button {
		:deep(path) {
			fill: $primary;
		}
	}

	&__button + &__button {
		margin-left: 15px;
	}
}
</style>
