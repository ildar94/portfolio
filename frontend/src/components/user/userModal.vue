<template>
	<teleport to="body">
		<Modal class="userModal" :show="showModal" :title="title" @close="$emit('close')">
			<form class="form" :class="isSignUp ? 'form_wide' : ''" @submit.prevent="onSubmit">
				<template v-if="isSignUp">
					<div class="form__row">
						<label class="form__field form__field_alert">
							<AppInput v-model="userData.name" type="text" placeholder="Введите Имя *" />
							<span class="form__error alert alert_small alert_danger" :class="isValidationActive && !validation.name.isValid ? 'active' : ''">
								{{ validation.name.error }}
							</span>
						</label>
						<label class="form__field">
							<AppInput v-model="userData.surname" type="text" placeholder="Введите Фамилию" />
						</label>
					</div>
					<div class="form__row">
						<label class="form__field form__field_alert">
							<AppInput v-model="userData.email" placeholder="Введите эл. почту *" inputmode="email" autocomplete="username" />
							<span class="form__error alert alert_small alert_danger" :class="isValidationActive && !validation.email.isValid ? 'active' : ''">
								{{ validation.email.error }}
							</span>
						</label>
						<label class="form__field form__field_alert">
							<AppInput v-model="userData.phone" inputmode="numeric" placeholder="Введите телефон *" v-maska="phoneObject" data-maska="+7 (###)-###-##-##" />
							<span class="form__error alert alert_small alert_danger" :class="isValidationActive && !validation.phone.isValid ? 'active' : ''">
								{{ validation.phone.error }}
							</span>
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
							<AppInput v-model="userData.password" type="password" placeholder="Введите пароль *" autocomplete="new-password" />
							<span class="form__error alert alert_small alert_danger" :class="isValidationActive && !validation.password.isValid ? 'active' : ''">
								{{ validation.password.error }}
							</span>
						</label>
						<label class="form__field form__field_alert">
							<AppInput v-model="userData.passwordRetry" type="password" placeholder="Повторите пароль *" autocomplete="new-password" />
							<span class="form__error alert alert_small alert_danger" :class="isValidationActive && !validation.passwordRetry.isValid ? 'active' : ''">
								{{ validation.passwordRetry.error }}
							</span>
						</label>
					</div>
					<div class="userModal__row">
						<AppButton class="userModal__button" color="white" :icon="true" @click="changeTemplate(false)">
							<template #icon>
								<ArrowLeftIcon fill="none" />
							</template>
							Назад
						</AppButton>
						<AppButton class="userModal__button" color="secondary" type="submit">Зарегистрироваться</AppButton>
					</div>
				</template>
				<template v-else>
					<label class="form__field form__field_alert">
						<AppInput v-model="userData.email" inputmode="email" placeholder="Введите эл. почту *" autocomplete="username" />
						<span class="form__error alert alert_small alert_danger" :class="isValidationActive && !validation.email.isValid ? 'active' : ''">
							{{ validation.email.error }}
						</span>
					</label>
					<label class="form__field form__field_alert">
						<AppInput v-model="userData.password" type="password" placeholder="Введите пароль *" autocomplete="current-password" />
						<span class="form__error alert alert_small alert_danger" :class="isValidationActive && !validation.password.isValid ? 'active' : ''">
							{{ validation.password.error }}
						</span>
					</label>
					<div class="userModal__row">
						<AppButton class="userModal__button" color="secondary" type="submit">Войти</AppButton>
						<AppButton class="userModal__button" color="white" @click="changeTemplate(true)">Нет еще аккаунта? Зарегистрируйтесь</AppButton>
					</div>
				</template>
			</form>
		</Modal>
	</teleport>
</template>

<script lang="ts">
import { defineComponent, ref, computed, reactive, ComputedRef, Ref } from 'vue';
import Modal from '@/components/modal.vue';
import AppInput from '@/components/form/input.vue';
import AppButton from '@/components/button/index.vue';
import ArrowLeftIcon from '@/components/icons/arrowLeftIcon.vue';
import { minLength, isEqual, isValidEmail, required } from '@/utils/validation';
import { useValidation, schemeI } from '@/composables/validation';
import { UserAuthI } from '@/api/user/types';
import { vMaska, MaskaDetail } from 'maska';

export default defineComponent({
	name: 'userModal',
	emits: ['close'],
	props: {
		showModal: {
			type: Boolean,
			default: false,
		},
	},
	directives: {
		maska: vMaska,
	},
	setup() {
		const isAuth = ref(false);
		const isSignUp = ref(true);
		const title = computed(() => isSignUp.value ? 'Регистрация' : 'Вход в личный кабинет');

		function changeTemplate(signUp: boolean) {
			isSignUp.value = signUp;

			userData.password = '';
			userData.email = '';

			isValidationActive.value = false;
		}

		const isValidationActive = ref(false);

		const phoneObject: Ref<MaskaDetail> = ref({
			masked: '',
			unmasked: '',
			completed: false,
		});

		const userData: UserAuthI = reactive({
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

		const validationScheme: ComputedRef<schemeI> = computed(() => ({
			name: [{ fn: required, errorMessage: 'Имя обязательно для заполнения' }],
			email: [
				{ fn: required, errorMessage: 'Эл. почта обязательна для заполнения' },
				{ fn: isValidEmail, errorMessage: 'Не валидный формат Эл. почты' },
			],
			phone: [
				{ fn: required, errorMessage: 'Телефон обязателен для заполнения' },
				{ fn: () => phoneObject.value.completed, errorMessage: 'Не валидный формат телефона' },
			],
			password: [
				{ fn: required, errorMessage: 'Пароль обязателен для заполнения' },
				{ fn: minLength, params: [8, userData.password], errorMessage: 'Пароль должен содержать не менее 8 символов' },
			],
			passwordRetry: [
				{ fn: required, errorMessage: 'Повторный пароль обязателен для заполнения' },
				{ fn: isEqual, params: [userData.password, userData.passwordRetry], errorMessage: 'Пароли не совпадают' },
			],
		}));

		const validation = useValidation(userData, validationScheme);

		function onSubmit() {
			isValidationActive.value = true;

			if (!isSignUp.value && validation.email.isValid && validation.password.isValid) {
				console.log(1);
			}

			if (isSignUp.value && !Object.values(validation).find(item => !item.isValid)) {
				console.log(2);
			}
		}

		return {
			isAuth,
			isSignUp,
			title,
			changeTemplate,
			userData,
			phoneObject,
			validation,
			isValidationActive,
			onSubmit,
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
	&__row {
		display: flex;
		margin-top: 30px;
	}

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
