<template>
  <div class="form-structor">
    <div class="signup">
      <h2 id="signup" class="form-title">
        <span>or</span>Sign up
      </h2>
      <div class="form-holder">
        <input type="text" class="input" placeholder="Nickname"  v-model="nickname" />
        <input type="email" class="input" placeholder="Email" v-model="email"/>
        <input type="password" class="input" placeholder="Password" v-model="password"/>
        <input type="number" class="input" placeholder="Age" min="0" max="100" v-model="age">
        <div class="input radio_div">
          <label for="gender" class="radio_label">Gender</label>
          <div class="radio_btn_div">
            <div>
                F
                <input type="radio" name="gender" value="F" v-model="gender"/>
            </div>
            <div>
                M
                <input type="radio" name="gender" value="M" v-model="gender"/>
            </div>
        </div>
      </div>
    </div>
    <button class="submit-btn" @click="OnSubmitSignUp">Sign up</button>
    </div>
    <div class="login slide-up">
      <div class="center">
        <h2 id="login" class="form-title">
          <span>or</span>Log in
        </h2>
        <div class="form-holder">
          <input type="email" class="input" placeholder="Email" v-model="email" />
          <input type="password" class="input" placeholder="Password" v-model="password" />
        </div>
        <button class="submit-btn" @click="OnSubmitLogIn">Log in</button>
      </div>
    </div>
  </div>
</template>

<script>
import { mapActions } from "vuex";

export default {
  data() {
    return {
      email: null,
      password: null,
      nickname: null,
      gender: null,
      age: null,
    }
  },
  methods: {
    OnSubmitSignUp(){
      const params = {
        email: this.email,
        password: this.password,
        nickname: this.nickname,
        gender: this.gender,
        age: this.age
      }
      this.signUp(params);
	},
    OnSubmitLogIn(){
      const params = {
        email: this.email,
        password: this.password,
      }
      this.logIn(params);
    },
    ...mapActions("data", ["logIn"]),
    ...mapActions("data", ["signUp"]),
  },
  mounted() {
    const loginBtn = document.getElementById("login");
    const signupBtn = document.getElementById("signup");

    loginBtn.addEventListener("click", e => {
      let parent = e.target.parentNode.parentNode;
      Array.from(e.target.parentNode.parentNode.classList).find(element => {
        if (element !== "slide-up") {
          parent.classList.add("slide-up");
        } else {
          signupBtn.parentNode.classList.add("slide-up");
          parent.classList.remove("slide-up");
        }
      });
    });

    signupBtn.addEventListener("click", e => {
      let parent = e.target.parentNode;
      Array.from(e.target.parentNode.classList).find(element => {
        if (element !== "slide-up") {
          parent.classList.add("slide-up");
        } else {
          loginBtn.parentNode.parentNode.classList.add("slide-up");
          parent.classList.remove("slide-up");
        }
      });
    });
  }
};
</script>
